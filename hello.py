def application(env, start_responce):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	body = [bytes(i+'\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	start_responce(status, headers)
	return body
