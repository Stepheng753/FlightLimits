export function fetch_post(api_link, body, afterFunc) {
	fetch(api_link, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: body,
	})
		.then((res) => res.json())
		.then((data) => afterFunc(data));
}
