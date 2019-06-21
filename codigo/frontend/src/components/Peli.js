// components/Peli.js
import React, { Component } from 'react'

export default class Peli extends Component {

	render() {

	var peli = this.props.peli   // props desde el componente de arriba
	return(
	   <div key={peli.id}>
	      <h3>{peli.title}</h3>

	      <hr />
	   </div>
	  )
	}
}
