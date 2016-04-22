Title: Catch invalid hosts before Django's ALLOWED_HOSTS
Date: 2016-04-22
Category: Achievements
Tags: python, django, nginx, security

I have been haunted all these years by the "Invalid HTTP_HOST header" error
email that [Django sends to its `ADMINS`][4] when an user -- or a script, most
likely -- tries to access the application with an invalid host header.

Every day I had to mark and delete tons of alert emails. What annoying. But
then I researched about it and found an [answer like this one][1]. Happy as I
was, I immediately wrote those settings into my nginx configuration file and
boom! Next day I still had tons of emails to mark and delete. After testing
some other configurations based on the same idea, I then accepted that as a
daily burden. How frustrating.

But that had to die. Technology exists for a reason: solve problems. Reading
the [nginx's `ngx_http_rewrite_module` documentation][2], I found out the `if`
statement. That was just too obvious, but no one mentioned it. Perhaps due to
[its caveats][3]. But hey, with a bit of care, it worked flawlessly:

	:::nginx
	location / {
		# Handle unhandled vhosts
		if ($host != 'my-undisclosed-hostname.com') {
			return 400;
		}

		include fastcgi_params;
		include proxy_params;
		# ...
	}

Then I ran cURL with a custom Host header and the `if` statement proved to be
effective, finally.

	:::text
	$ curl -IH 'Host: something-else' http://my-undisclosed-hostname.com
	HTTP/1.1 400 Bad Request
	Server: nginx/1.8.1
	Content-Type: text/html
	Content-Length: 181
	Connection: close

Now I can get to spend one more minute every day with something else, yay.


[1]: http://stackoverflow.com/questions/17149435/avoiding-djangos-500-error-for-not-allowed-host-with-nginx
[2]: http://nginx.org/en/docs/http/ngx_http_rewrite_module.html#if
[3]: https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/
[4]: https://docs.djangoproject.com/en/1.9/howto/error-reporting/#server-errors
