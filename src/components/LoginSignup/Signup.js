import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Button } from "reactstrap";
import About from "../About";
import Navv from "../Navv";
import Footer from "../Footer";
const Signup = () => {
  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    if (formData.password !== formData.confirmPassword)
      alert("Passwords do not match");
    else console.log(formData);
  };
  const [formData, setFormData] = useState({
    fname: "",
    lname: "",
    contact: "",
    email: "",
    address: "",
    password: "",
    confirmPassword: "",
  });
  return (
    <div>
      <Navv />
      <h3>Sign up and bid away!</h3>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="FirstName">First Name</Label>
          <Input
            id="FirstName"
            name="fname"
            placeholder="First Name"
            type="text"
            value={formData.fname}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="LastName">Last Name</Label>
          <Input
            id="LastName"
            name="lname"
            placeholder="Last Name"
            type="text"
            value={formData.lname}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Contact">Contact</Label>
          <Input
            id="Contact"
            name="contact"
            placeholder="Contact"
            type="text"
            value={formData.contact}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Email">Email</Label>
          <Input
            id="Email"
            name="email"
            placeholder="Enter your email here"
            type="email"
            value={formData.email}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Address">Address</Label>
          <Input
            id="Address"
            name="address"
            placeholder="Address"
            type="textarea"
            value={formData.address}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Password">Password</Label>
          <Input
            id="Password"
            name="password"
            placeholder="password"
            type="password"
            value={formData.password}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="ConfirmPassword">Confirm Password</Label>
          <Input
            id="ConfirmPassword"
            name="confirmPassword"
            placeholder="Confirm your password"
            type="password"
            value={formData.confirmPassword}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <Button color="primary">Submit</Button>
      </Form>
      <br />
      <div style={{ marginLeft: "0.5rem" }}>
        <About />
      </div>
      <Footer />
    </div>
  );
};

export default Signup;
