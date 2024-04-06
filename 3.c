int
stravis(char **outp, const char *src, int flag)
{
	char *buf;
	int len, serrno;

	buf = calloc(4, strlen(src) + 1);
	if (buf == NULL)
		return -1;
	len = strvis(buf, src, flag);
	serrno = errno;
	*outp = realloc(buf, len + 1);
	if (*outp == NULL) {
		*outp = buf;
		errno = serrno;
	}
	return (len);
}