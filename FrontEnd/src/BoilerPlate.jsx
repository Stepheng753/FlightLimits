import { useState } from 'react';
import { signal } from '@preact/signals-react';
import { Navigate } from 'react-router-dom';
import reactLogo from './assets/react.svg';
import viteLogo from './assets/vite.svg';
import './css/App.css';

function BoilerPlate() {
	const count = signal(0);
	const [redirect, setRedirect] = useState(false);

	if (redirect == true) {
		return <Navigate to={'payment-portal'} />;
	}

	return (
		<>
			<div>
				<a href="https://vitejs.dev" target="_blank">
					<img src={viteLogo} className="logo" alt="Vite logo" />
				</a>
				<a href="https://react.dev" target="_blank">
					<img src={reactLogo} className="logo react" alt="React logo" />
				</a>
			</div>
			<h1>Vite + React</h1>
			<button onClick={() => setRedirect(!redirect)}>
				<h3>Click Here for Payment Portal</h3>
			</button>
			<div className="card">
				<button onClick={() => count.value++}>count is {count}</button>
				<p>
					Edit <code>src/Home.jsx</code> and save to test HMR
				</p>
			</div>
			<p className="read-the-docs">Click on the Vite and React logos to learn more</p>
		</>
	);
}

export default BoilerPlate;
