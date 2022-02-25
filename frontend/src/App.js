import logo from './logo.svg';
import './App.css';
import { Link } from 'react-router-dom';
import React, {useEffect, useState} from 'react';
import axios from 'axios'
//import Login from "./Login"

function App() {
//  return (
//    <div>
//      <h1>Bookkeeper</h1>
//      <nav
//        style={{
//          borderBottom: "solid 1px",
//          paddingBottom: "1rem"
//        }}
//      >
//        <Link to="/login">Login</Link> |{" "}
//      </nav>
//    </div>
//);


//    <Route exact path="/login">
//      <Login />
//    </Route>
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:3000/react').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React + Flask Tutorial</p>
        <div>{getMessage.status === 200 ?
          <div>
          <h3>{getMessage.data.message}</h3>
          <Link to="/login">Login</Link> |{" "}
          </div>
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default App;
