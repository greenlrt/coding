/* client.c - Create socket */

#include "socket.h"

int main(int argc, char *argv[]) {
	int s;
	char server[] = "man7.org";
	int port = 80;
	struct hostent *host;
	struct sockaddr_in addr;
	char *request;
	char result[4096];
	printf("start");
	s = socket(AF_INET, SOCK_STREAM, 0);
	printf("here");
	host = gethostbyname(server);

	request = malloc(25 + strlen(server));
	
	sprintf(request, "GET / HTTP/1.1\nHost: %s\n\n", server);

	/*memset((char *) &addr, 0, sizeof(struct sockaddr_in));*/
	addr.sin_family = AF_INET;
	addr.sin_port = htons(port);
	addr.sin_addr = *((struct in_addr *) host->h_addr);

	connect(s, (struct sockaddr *) &addr,
			sizeof(struct sockaddr));
	send(s, (void *) request, strlen(request), NULL);
	recv(s, result, strlen(result) - 1, NULL);

	while(strlen(result) > 0) {
		printf(result);
		recv(s, result, strlen(result) - 1, NULL);
	}

	free(request);
	close(s);
	return 0;

}
