import { useState } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { MainImage } from '../Globals/Globals';
import duffelLogo from '../assets/duffel.png';

function Success(props) {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const location = useLocation();
	let order = location.state.data;

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	return (
		<div>
			<MainImage redirectFunc={setRedirect} />
			<a href="https://app.duffel.com/c9b5c49110322475ef39788/test/orders" target="_blank">
				<img src={duffelLogo} className="logo" alt="Duffel logo" />
			</a>
			<h1>Success!</h1>
			<br />
			<h3>{order.id}</h3>
		</div>
	);
}

export default Success;
