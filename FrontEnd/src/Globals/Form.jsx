export function form(inputs, setInputsFunc) {
	let form = [];
	for (let i = 0; i < inputs.length; i++) {
		let input = inputs[i];
		form.push(
			<div key={i}>
				<label>
					{input.label}:{' '}
					<input
						type={input.type}
						value={input.value}
						onChange={(e) => {
							let new_arr = [...inputs];
							new_arr[i].value = e.target.value;
							setInputsFunc(new_arr);
						}}
						min={input.min}
					/>
				</label>
				<br />
			</div>
		);
	}
	return <form>{form}</form>;
}

export function convertFormDataToJSON(formData) {
	let rtnJSON = { indices: {}, data: formData };
	for (let i = 0; i < formData.length; i++) {
		rtnJSON.indices[formData[i].label] = i;
	}
	return rtnJSON;
}
