import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import '../css/App.css';
import airplane from '../assets/airplane.gif';

function SearchFlights() {
	const [redirect, setRedirect] = useState({ to: '' });

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} />;
	}

	function test_pg(body) {
		fetch('/api/post_test', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ TEST1: 'TEST1' }),
		})
			.then((res) => res.text())
			.then((data) => console.log(data));
	}

	return (
		<div>
			<div>
				<img
					src={airplane}
					className="logo airplane"
					alt="Flight Limits"
					onClick={() => setRedirect({ to: '/' })}
				/>
			</div>
			<h1>Search Flights</h1>
			<br />
			<button onClick={() => test_pg('Hello')}>
				<h3>TEST PG</h3>
			</button>
			<br />
		</div>
	);
}

export default SearchFlights;
