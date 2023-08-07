// Importing modules
import React, { useState, useEffect } from "react";
import ScriptForm from "./components/ScriptForm";
import "./App.css";
 
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    // const [data, setdata] = useState({
    //     name: "",
    //     age: 0,
    //     date: "",
    //     programming: "",
    // });
 
    // // Using useEffect for single rendering
    // useEffect(() => {
    //     // Using fetch to fetch the api from
    //     // flask server it will be redirected to proxy
    //     fetch("/data").then((res) =>
    //         res.json().then((data) => {
    //             // Setting a data from api
    //             setdata({
    //                 name: data.Name,
    //                 age: data.Age,
    //                 date: data.Date,
    //                 programming: data.programming,
    //             });
    //         })
    //     );
    // }, []);
 
    return (
        <div className="App">
            <header className="App-header">
                <h1>AI SPARC Flows</h1>
                <ScriptForm/>
            </header>
        </div>
    );
}
 
export default App;