class ClickButton extends React.Component {
  state = {
    wasClicked : false
  }

  handelClick () {
    this.setState(
      {wasClicked: !this.state.wasClicked}
    )
    console.log('Click me');
  }

  render () {
    let buttonText;
    if (this.state.wasClicked) {
      buttonText = 'Clicked';
    } else {
      buttonText = 'Click Me';
    }

    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: () => {
          this.handelClick()
        }
      },
      buttonText
    )
  }
}

const domContainer = document.getElementById('react_root');
ReactDOM.render(
  React.createElement(ClickButton),
  domContainer
)
