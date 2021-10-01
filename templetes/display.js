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


// function display(data) {

//   var img = document.createElement('img'); 
//   img.className += "type1";
//   img.src = "http://127.0.0.1:8080/data/photo/"+data.id; 
//   document.getElementById('avatar').appendChild(img);

//   document.getElementById("name").innerHTML = data.name;
//   document.getElementById("id").innerHTML = "ID - "+data.id;
//   document.getElementById("dob").innerHTML = "DOB - "+data.dob;
//   document.getElementById("dept").innerHTML = "Department - "+data.dept;

// }

function display(data) {
    for (var key in data) {
        var name = data[key][2];
        var id = data[key][1];
        var dept = data[key][3];  
        const d = new Date();
        document.getElementById("tdy").innerHTML = d.toDateString();
        
        const view = document.createElement('div');
        view.innerHTML = `
        <div class="row">
            <div class="column">
                <div class="card">
                    <img class="type1" src="http://127.0.0.1:8080/data/photo/${id}"> 
                    <h1 id="name">${name}</h1>
                    <h2 id="id">UID : ${id}</h2>
                    <h2 id="dob">${dept}</h2>
                </div>
            </div>      
        </div> 
        `
        main.appendChild(view);
    }

}