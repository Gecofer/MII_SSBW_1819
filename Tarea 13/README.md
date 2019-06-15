## Tarea 13: Single Page Application con React

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%2013/Tarea13.md) para ver cómo se hizo la Tarea 13**

## Back-end
En esta tarea haremos un front-end con [React](https://reactjs.org) para el API de la práctica anterior siguiendo [Django Rest Framework with React Tutorial](https://wsvincent.com/django-rest-framework-react-tutorial/).

El único cambio que hacemos en el back-end es instalar **django-cors-headers**, y ponerlo en 'settings.py' tal como indica, excepto

~~~python
CORS_ORIGIN_WHITELIST = [
		'http://localhost:3000'
]
~~~

El paquete sirve para que se pueda acceder a la aplicación desde otro dominio, lo que normalmente no está permitido por razones de seguridad. Aunque no hará falta en el servidor de producción, siempre que se sirva la aplicación desde el mismo servidor que el resto del back-end.


### Front-end

El front-end es 'solamente' una página web con javascript, así que lo podemos lanzar desde nuestro host sin que intervenga un contenedor docker o una máquina virtual. Haremos el front-end en dos pasos, primero comprobamos que funciona una aplicación mínima que se conecte con django como está en el tutorial, y luego incorporaremos los demás componentes, con

Instalamos todo el [ecosistema de react](https://www.toptal.com/react/navigating-the-react-ecosystem) con [create-react-app](https://www.npmjs.com/package/create-react-app), que además incluye un servidor de desarrollo.

~~~
> sudo npm install -g create-react-app
> create-react-app frontend
> cd frontend
> npm install react-router-dom
> npm install bootstrap
> npm install reactstrap
> npm start
~~~

e instalamos bootstrap para react, tal como viene en [reacstrap](https://reactstrap.github.io). Incluimos también **react-router**, tal como en [react trainig / reac router](https://reacttraining.com/react-router/core/guides/philosophy). Ampliamos entonces el archivo **index.js** para incluir el router y bootstrap

~~~python
// src/index.js
import { BrowserRouter } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';

...

ReactDOM.render(
	<BrowserRouter>
		<App />
	</BrowserRouter>
, document.getElementById('root'))
registerServiceWorker()
~~~~

Para ser ordenados, creamos un nuevo directorio **components**, para poner aparte todos los componentes de nuestra aplicación. El principal **App.js** quedaría, con [navbar](https://reactstrap.github.io/components/navbar/) de reacstrap:

~~~python
// components/App.js
import React, { Component } from 'react'
import {Route} from 'react-router-dom'
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem } from 'reactstrap';

// Para visualizar la lista de películas
import Todas from '.components/Todas'

export default class Example extends React.Component {

  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }

  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }

  render() {
    return (
      <div>                                              // Código JSX
        <Navbar color="light" light expand="md">
          <NavbarBrand href="/">reactstrap</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              <NavItem>
                <NavLink href="/components/">Components</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="https://github.com/reactstrap/reactstrap">GitHub</NavLink>
              </NavItem>
              <UncontrolledDropdown nav inNavbar>
                <DropdownToggle nav caret>
                  Options
                </DropdownToggle>
                <DropdownMenu right>
                  <DropdownItem>
                    Option 1
                  </DropdownItem>
                  <DropdownItem>
                    Option 2
                  </DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem>
                    Reset
                  </DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
            </Nav>
          </Collapse>
        </Navbar>
      <br/><br/>
			 <Route path="/todas" component={Todas}/>
      </div>
    );
  }
}
~~~

El componente `Todas`, hará una llamada GET al API, para traerse una lista de las diez primeras películas justo después de montarse. ([React js y el ciclo de vida de los componentes](https://medium.com/@pedroparra/react-js-y-el-ciclo-de-vida-de-los-componentes-5d083e5089c6)). Creamos una nueva clase `Component` de react en un archivo:

~~~python
// components/Todas.js
import React, { Component } from 'react'
import Peli from './Peli'

export default class Todas extends Component {
  constructor(props) {
    super(props)
    this.state = {                // variable estado de la clase, lista de películas
      pelis: []
     }
  }

// llamada al API
componentDidMount() {
  fetch('https://localhost/miapp/api/pelis/?format=json')  // o el que sea
    .then(res => { return res.json()})
    .then(data => {
      console.log(data)
      this.setState({pelis:data})
    }).catch(error => {
      console.log(error)
    })

  }

  render() {
    // re-renderiza al cambiar el state
    return (
      <div>
        Todas las pelis: <br />
        {this.state.pelis.map(peli => {  // arrow function
          return (
            <Peli peli={peli} />
          )
        })
      }
      </div>
    )
  }
}
~~~

Aqui se llama a otro componente, `Peli`, para mostrar los detalles de cada pelicula

~~~python
// components/Peli.js
import React, { Component } from 'react'

export default Peli extends Component {

	render() {

	var peli = this.props.peli   // props desde el componente de arriba
	return(
	   <div key={peli.id}>
	      <h3>{peli.name}</h3>
...
	      <hr />
	   </div>
	  )
	}
}
~~~
