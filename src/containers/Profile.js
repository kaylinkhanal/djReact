import React from 'react';
import {connect} from 'react-redux';

class Profile extends React.PureComponent{
  render(){
        return <div> Hi {this.props.username}</div>;
  }
}

const mapStateToProps =state =>{
  return {
    token:state.auth.token,
    username:state.auth.username
  }
}

const mapDispatchTOProps =dispatch =>{
  return{
    //
  }
}

export default connect(mapStateToProps,mapDispatchTOProps)(Profile);
