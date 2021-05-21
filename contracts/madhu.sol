
pragma solidity 0.5.16;

contract madhu {

	uint[] a;

	function insertSensorValue(uint m) public {
		a.push(m);
	}

	function getLastSensorValue() public view returns(uint) {
		return(a[a.length-1]);
	}
}
