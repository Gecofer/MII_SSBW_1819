## Tarea 13: Single Page Application con React

instalamos en el requirements: django-cors-headers

y hacemod docker-compose build

luego nos vamos a settings y añadimos

INSTALLED_APPS = [
    'corsheaders'
]

Está siguiendo este enlace: https://wsvincent.com/django-rest-framework-react-tutorial/, aunque está antiguado,
Lo único que nos hemos hecho han sido los tests

Hay que ponerlo en el MIDDLEWARE

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # new
    'django.middleware.common.CommonMiddleware', # new
    ...
]

y hay que añadir

CORS_ORIGIN_WHITELIST = [
		'http://localhost:3000'
]


Lo que v hacer que no sea llamado, desde el propio de la aplicación

Hay que instalar todo el ecosistema de react
Instalamos todo el ecosistema de react con create-react-app, que además incluye un servidor de desarrollo.

Enla carpeta de codigo, que es la que me interesa

> sudo npm install -g create-react-app
> create-react-app frontend
> cd frontend
> npm install react-router-dom
> npm install bootstrap
> npm install reactstrap
> npm start

----

cvi087249:MII_SSBW_1819 gema$ sudo npm install -g create-react-app
Password:
/usr/local/bin/create-react-app -> /usr/local/lib/node_modules/create-react-app/index.js
+ create-react-app@3.0.1
added 91 packages from 45 contributors in 6.513s
cvi087249:MII_SSBW_1819 gema$ cd codigo/
cvi087249:codigo gema$ sudo npm install -g create-react-app
/usr/local/bin/create-react-app -> /usr/local/lib/node_modules/create-react-app/index.js
+ create-react-app@3.0.1
updated 1 package in 1.312s


   ╭───────────────────────────────────────────────────────────────╮
   │                                                               │
   │       New minor version of npm available! 6.5.0 → 6.9.0       │
   │   Changelog: https://github.com/npm/cli/releases/tag/v6.9.0   │
   │               Run npm install -g npm to update!               │
   │                                                               │
   ╰───────────────────────────────────────────────────────────────╯

cvi087249:codigo gema$ npm install -g npm
/usr/local/bin/npm -> /usr/local/lib/node_modules/npm/bin/npm-cli.js
/usr/local/bin/npx -> /usr/local/lib/node_modules/npm/bin/npx-cli.js
+ npm@6.9.0
added 52 packages from 9 contributors, removed 15 packages and updated 37 packages in 9.156s
cvi087249:codigo gema$ create-react-app frontend

Creating a new React app in /Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend.

Installing packages. This might take a couple of minutes.
Installing react, react-dom, and react-scripts...


> fsevents@1.2.9 install /Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend/node_modules/chokidar/node_modules/fsevents
> node install

[fsevents] Success: "/Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend/node_modules/chokidar/node_modules/fsevents/lib/binding/Release/node-v67-darwin-x64/fse.node" is installed via remote

> fsevents@1.2.9 install /Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend/node_modules/jest-haste-map/node_modules/fsevents
> node install

[fsevents] Success: "/Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend/node_modules/jest-haste-map/node_modules/fsevents/lib/binding/Release/node-v67-darwin-x64/fse.node" is installed via remote

> core-js@2.6.9 postinstall /Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend/node_modules/babel-runtime/node_modules/core-js
> node scripts/postinstall || echo "ignore"


> core-js-pure@3.1.3 postinstall /Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend/node_modules/core-js-pure
> node scripts/postinstall || echo "ignore"

+ react@16.8.6
+ react-scripts@3.0.1
+ react-dom@16.8.6
added 1541 packages from 747 contributors and audited 888971 packages in 75.118s
found 0 vulnerabilities


Success! Created frontend at /Users/gema/Documents/Github/MII_SSBW_1819/codigo/frontend
Inside that directory, you can run several commands:

  npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd frontend
  npm start

Happy hacking!

-----------------------------


> cd frontend
> npm install react-router-dom
> npm install bootstrap
> npm install reactstrap
> npm start


hacemos npm start y no abre en http://localhost:3000/



Y enla carpeta frontend > src > App.js

import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
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
  );
}

export default App;

---

Y si cambio: Learn React y lo modifico se cambia

Nos salimos ctrol+c

Ahora nos tenemos que instalar

> npm install react-router-dom
> npm install bootstrap
> npm install reactstrap

Hemos instalado todo esto

e instalamos bootstrap para react, tal como viene en reacstrap. Incluimos también react-router, tal como en react trainig / reac router. Ampliamos entonces el archivo index.js para incluir el router y bootstrap


frontend > src > index.js --> este fichero es el primero que ejecuta

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();


y añadimos

import { BrowserRouter } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';


y quedaría:

~~~~
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import { BrowserRouter } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';

// ReactDOM.render(<App />, document.getElementById('root'));

ReactDOM.render(
	<BrowserRouter>
		<App />
	</BrowserRouter>,
    document.getElementById('root'))


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
~~~~

esto 	<BrowserRouter> lo que hace es llamar a la Appp.js

y luego copio y pego de aquí: https://reactstrap.github.io/components/navbar/

Las variables globales que vamos a usar es


He puesto el navbar del bootstrap

export default class App extends React.Component {

  // aquí va la clase del navbar: https://reactstrap.github.io/components/navbar/

  // el constructor lo que hace es poner la variable this.toggle.bind(this)
  // como unas variables globales

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

  // y nos falta el return que es el que dibuja
  render() {
    return (
      <div>
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
        <div class="container">
          Aqui ponemos más componentes
        </div>

      </div>
    );
  }

}

y vamos a la API, y nos extraemos los


Ahora va hacer ese componente de "todas"

Nos creamos dentro de "src" una carpeta de components

me creo un fichero Todas.js que tengo que llamar en App.js con (import Todas from './components/Todas')


--------

Hay que hacer una tarea 14 de depliegue

en el docker-compose se cambiaria lo de
python manage.py runserver 0.0.0.0:8000

en lugar de poner runserver, hay que bajarse otro servidor, gunicorn seguramente, ponerlo en el requirements, y eso engancha a composeexample > wsgi.py

además en el settings se añadiria

DEBUG=False

https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/gunicorn/


cuando haya un error que la aplicación la arranque y funcione, que haya un proceso superusado, lo normal es ponerlo en el systemctl de unix
