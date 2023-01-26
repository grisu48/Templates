FROM registry.opensuse.org/opensuse/leap
LABEL maintainer="phoenix"
LABEL description="Hello world nginx docker"

#ARG VAULT_ADDR                  # Add custom argument to build
#ENV VAULT_ADDR=${VAULT_ADDR}    # Add environment variable


# docker image build breaks, if command does not exit with code 0
RUN rm -rf /var/cache/zypper

# Copy just copies the file, ADD deploys the file (i.e. uncompress to image)
# ADD also supports remote URIs
COPY whole-folder/ /where/to/copy/
COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/default.conf /etc/nginx/conf.d/default.conf
ADD files/html.tar.gz /usr/share/nginx/

VOLUME /data

EXPOSE 80/tcp

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
