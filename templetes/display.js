// api url
const api_url = "http://127.0.0.1:8080/fetch";
getapi(api_url); 

// Defining async function
async function getapi(url) {
fetch(url).then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
    display(data)
  });     
}   


function display(data) {

  var img = document.createElement('img'); 
  img.className += "type1";
  img.src = "http://127.0.0.1:8080/data/photo/"+data.id; 
  document.getElementById('avatar').appendChild(img);

  document.getElementById("name").innerHTML = data.name;
  document.getElementById("id").innerHTML = "ID - "+data.id;
  document.getElementById("dob").innerHTML = "DOB - "+data.dob;
  document.getElementById("dept").innerHTML = "Department - "+data.dept;

}