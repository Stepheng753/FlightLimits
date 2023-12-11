import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import githubLogo from './assets/github.png';
import duffelLogo from './assets/duffel.png';
import './css/App.css';

function Home() {
	const [redirect, setRedirect] = useState({ to: '' });
	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} />;
	}

	return (
		<>
			<div>
				<a href="https://github.com/Stepheng753/FlightLimits" target="_blank">
					<img src={githubLogo} className="logo" alt="Github logo" />
				</a>
				<a href="https://duffel.com/docs/guides/getting-started-with-flights" target="_blank">
					<img src={duffelLogo} className="logo" alt="Duffel logo" />
				</a>
			</div>
			<h1>Flight Limits</h1>
			<button onClick={() => setRedirect({ to: '/payment-portal' })}>
				<h3>Click Here for Payment Portal</h3>
			</button>
			<br />
			<br />
			<button onClick={() => setRedirect({ to: '/search-flights' })}>
				<h3>Click Here to Search Flights</h3>
			</button>
		</>
	);
}

export default Home;
