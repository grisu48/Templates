/* Simple mosquitto subscriber in GO
 * See https://gist.github.com/grisu48/9de045bce4247d50209748c5e134542f
 */

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	MQTT "github.com/eclipse/paho.mqtt.golang"
)

func onMessageReceived(client MQTT.Client, message MQTT.Message) {
	fmt.Printf("%s\t\t%s\n", message.Topic(), message.Payload())
}

func main() {
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)

	// Server and topic
	server := "127.0.0.1:1883"
	topic := "#"

	connOpts := MQTT.NewClientOptions().AddBroker(server)
	connOpts.OnConnect = func(c MQTT.Client) {
		if token := c.Subscribe(topic, byte(0), onMessageReceived); token.Wait() && token.Error() != nil {
			panic(token.Error())
		}
	}

	client := MQTT.NewClient(connOpts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		panic(token.Error())
	} else {
		fmt.Printf("Connected to %s\n", server)
	}

	<-c
}
