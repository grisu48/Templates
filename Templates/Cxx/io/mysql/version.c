
/* ==== MYSQL trivial implementation ===========================================
 * 
 * 
 * 
 * Compile with
 * - gcc -c -I/usr/include/mysql -Wall -Werror -pedantic -std=c99 version.c -o 
 *     version.obj
 * - gcc version.obj -L/usr/lib/mysql -lmysqlclient -o version
 * 
 * 
 * 
 * 
 * ========================================================================== */


#include <stdio.h>
#include <stdlib.h>
#if defined __WIN32__ || _MSC_VER
   #include "my_global.h"
   #include "mysql.h"
#else
   #include <mysql.h>
#endif


static MYSQL *my;

int main(int argc, char** argv)
{
    const char* host = "localhost";
    const char* user = "test";
    const char* password = "";
    const char* database = "";
    const int port = 0;       /* Default port */
    const int flags = 0;

    my = mysql_init(NULL);
    if(my == NULL) {
        fprintf(stderr, " MySQL initialisation failure \n");
        return EXIT_FAILURE;
    }

    /* mit dem Server verbinden */
    if( mysql_real_connect ( my, host, user, password, database, port,
        NULL  /* Socket, if any (default=NULL) */, flags  )  == NULL) {
        
        fprintf (stderr, "Error while connecting: " "%u (%s)\n",mysql_errno(my),
            mysql_error (my));
        return EXIT_FAILURE;
    }
    
    // Do usefull stuff
    
    
    
    mysql_close (my);
    return EXIT_SUCCESS;
}


