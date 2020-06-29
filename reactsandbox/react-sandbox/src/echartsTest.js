import React from 'react'
import logo from './logo.svg'
import doSth1 from "./myFunction"
import './App.css'
// Install material-ui: https://material-ui.com/
// Using a named import
import { Button, Slider } from '@material-ui/core'

// Using a default import
//import Button from '@material-ui/core/Button'
//import Slider from '@material-ui/core/Slider'


function sayHello() {
  console.log('%c hello', 'background: #0000ff; color: #ff00ff')
}

function MyComponent(props) {
  // 'props' is printed as [object Object] here because it's converted to
  // a string.
  console.log(`These are props as a string: ${props}`)
  // This prints the object
  console.log(props)
  // NOTE: The debugger statement only works if you have dev-tools open
  //debugger
  return <h1>Hello from MyComponent: {props.name}</h1>
}

class MyClassBasedComponent extends React.Component {
  constructor(props) {
    // Need to remember to call the parent constructor.
    super(props)
    // We create a state object and set our initial state in it
    this.state = {
      counter: 0,
      name: '',
      age: '',
      country: '',
      sliderValue: 0,
    }
  }

  // Remember to use Arrow Functions if you have problems with 'this' is not
  // defined
  increment = () => {
    this.setState({
      counter: this.state.counter + 1,
    })
  }

  handleInput = (e) => {
    console.log(`Input: ${e}`)
    // Remember to set 'name' prop on your input fields.
    this.setState({
      // This e.target.name is called a 'computed property names'
      [e.target.name]: e.target.value,
    })
  }

  handleSubmit = (e) => {
    // This stops the page from reloading upon submission
    e.preventDefault()
    // Use object destructuring
    const { name, age, country } = e.target
    console.log('Submitting form')

    // This works a bit like document.getElementById()
    console.log('Name element: ')
    console.log(name)
    console.log('Age element: ')
    console.log(age)
    console.log('Country element: ')
    // The long way of accessing it.
    console.log(e.target.elements.country)
    console.log('Form values: ')
    // NOTE: Notice how there is no country.value because we're not setting it?
    console.log(`Name: ${name.value} - Age: ${age.value} - Country: ${country.value}`)
    //debugger

    // Add a fetch() here and post the data to a website.
    const getUrl = 'http://httpbin.org/get'
    const postUrl = 'http://httpbin.org/post'

    const someObject = {
      someKey: 'Blah',
      name: name.value,
      // This is called object property shorthand.
      // Used if your key is the same name as the value
      age: age.value,
      country: 'dffdss',
    }

    // See https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
    console.log('Creating HTTP GET Request')
    fetch(getUrl)
      .then(response => {
        console.log(response)
        // Convert the response to JSON
        return response.json()
      })
      .then(data => {
        console.log('%c HTTP GET Response:', 'color: #f542e6')
        console.log(data)
      })

    console.log('Creating HTTP POST Request')
    fetch(postUrl, {
      method: 'POST',
      headers: {
        'My-Custom-Header': 'asdfd12343',
      },
      body: JSON.stringify(someObject),
    })
      // Arrow functions don't need 'return' if it's just 1 expression.
      .then(response => response.json())
      // You need to use braces if you have more than 1 expression though.
      .then(data => {
        console.log(`%c HTTP POST Response:`, 'color: #42b6f5')
        console.log(data)
      })


    // TODO: Make this post to your Django REST Framework API.
  }

  // Check the documentation for material-ui to see if you need 1 or
  // 2 parameters.
  handleSlider = (e, newValue) => {
    this.setState({
      sliderValue: newValue,
    })
    console.log(`New slider value: ${newValue}`)
  }

  render() {
    // This is called 'destructuring'. You can extract values from
    // objects/arrays using this technique.
    const { name, age } = this.state
    const { somePropCallback } = this.props
    // Remember to wrap your returns in a <div> if you have adjacent JSX
    // elements.
    return (
      <div>
        <h1>MyClassBasedComponent: {this.props.customProp}</h1>
        <h2>Counter: {this.state.counter}</h2>
        <h2>Name: {name}</h2>
        <h2>Age: {age}</h2>
        <h2>Country: {this.state.country}</h2>
        <button style={{color: "#ff0000"}} className="mybuttoncolor" onClick={this.increment}>Increment</button>

        <form onSubmit={this.handleSubmit}>
          {/* This is how you do a comment in JSX */}
          {/* Here we're setting value= on just the name field */}
          <input name="name" onChange={this.handleInput} placeholder="name" value={this.state.name} />
          <hr />
          <input name="age" onChange={this.handleInput} placeholder="age" value={age} />
          <hr />
          <input name="country" onChange={this.handleInput} placeholder="country" />
          <hr />
          <button type="submit">Submit</button>
          <hr />
          <Button onClick={somePropCallback}>Some Prop Callback Function</Button>
          <Slider value={this.state.sliderValue} onChange={this.handleSlider} />
        </form>
      </div>
    )
  }

}


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
          <MyClassBasedComponent customProp="1234" somePropCallback={sayHello} />
          <button onClick={doSth1}>DO DO DO</button>
          <MyComponent name="Blah" somemath={1 + 3} />
          <MyComponent name="Blah">These two lines are equivalent</MyComponent>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

// Files can only have 1 default export, but many named exports.
export default App
