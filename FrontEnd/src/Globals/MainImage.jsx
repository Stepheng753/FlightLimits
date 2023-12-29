import airplane from '../assets/airplane.gif';

function MainImage(props) {
	return (
		<img
			src={airplane}
			className="logo airplane"
			alt="Flight Limits"
			onClick={() => props.redirectFunc((prevRedirect) => ({ ...prevRedirect, to: '/' }))}
		/>
	);
}

export default MainImage;
