// App.js HW 14 Intro to JS
var tableData = data;

var tbody = d3.select("tbody");

function buildTable(data) {
	// clear out existing data
	tbody.html("");
	// loop through each roaw and append table
	data.forEach((dataRow) => {

		var row = tbody.append("tr");
		//  loop through each row value and append cell
		Object.values(dataRow).forEach((val) => {
			var cell = row.append("td");
			cell.text(val);
		})
	})
}

function handleClick() {
	d3.event.preventDefault();
	//  select the datetime value from the filter
	var date = d3.select("#datetime").property("value");
	let filteredData = tableData;
	//  filter the data based on the entered date
	if (date) {
		filteredData = filteredData.filter(row => row.datetime === date)

	buildTable(filteredData);
	}
}

d3.selectAll("#filter-btn").on("click",handleClick);

buildTable(tableData);