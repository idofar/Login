import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Login.css";
import axios from 'axios'

//export default function Login() {
//  console.log("in login!")
//  return (
//    <main style={{ padding: "1rem 0" }}>
//      <h2>Login!</h2>
//    </main>
//  );
//}

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function validateForm() {
    return email.length > 0 & password.length > 0;
  }

  function handleSubmit(event) {
    event.preventDefault();
    try {
    {/* need to send it in request form!!! because request data is just bytes */}
    const creds_form = {
    "username": email,
    "password" : password
    }
      axios.post("http://localhost:5000/login", creds_form).then(res => res.data).then(json => {
      console.log("results:", json.resultStatus, json.resultStatus.charCodeAt(7), "SUCCESS", "SUCCESS".charCodeAt(7), typeof json.resultStatus)
      if (json.resultStatus.replace(/\s+/g, "") === "SUCCESS") {
        alert("Logged in");
      } else {
        alert("Incorrect Credentials");
      }
      })
    } catch (e) {
      alert(e.message);
    }
  }

  return (
    <div className="Login">
      <Form onSubmit={handleSubmit}>
        <Form.Group size="lg" controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>
        <Form.Group size="lg" controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>
        <Button block_size="lg" type="submit" disabled={!validateForm()}>
          Login
        </Button>
      </Form>
    </div>
  );
}