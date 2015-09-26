
$(document).ready(function () {

  var AppContainer = React.createClass({

    render: function() {
      return (
        <div className="app-container">
          <div className="sidebar">
            This is a sidebar
          </div>
          <div className="content">
            <MapContainer lat={51.509746} lng={-0.118346} />
            <div className="graph-container">
              This is where the graph will live
            </div>
          </div>
        </div>
      );
    }
  });

  var MapContainer = React.createClass({

    getInitialState: function () {
      return {
        map: null,
        data: {}
      }
    },

    componentDidMount: function () {
      this.getStations();
    },

    getStations: function () {
      var _this = this;

      $.ajax({url: "/bikes", type: 'GET', dataType: 'json'})
        .done(function (data) {
          _this.setState({
            data: data
          });

          _this.drawMap();
          _this.drawStations();
        })
        .fail(function (xhr, textStatus, errorThrown) {
          console.log('ERROR: ', errorThrown);
        });
    },

    drawMap: function () {
      var _this = this;
      
      var map = new google.maps.Map(this.getDOMNode(), {
        center: {lat: _this.props.lat, lng: _this.props.lng},
        zoom: 13
      });

      this.setState({
        map: map
      })
    },

    drawStations: function () {
      var _this = this;

      console.log(this.state.data);

      Object.keys(this.state.data).forEach(function (k) {
        var marker = new google.maps.Marker({
          position: { lat: parseFloat(_this.state.data[k].lat), lng: parseFloat(_this.state.data[k].long) },
          map: _this.state.map,
          title: 'Hello World!',
          icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 4,
            strokeWeight: 4,
            strokeColor: "#34495e"
          }
        });
      })
    },

    render: function() {
      return (
        <div id="map-container" className="map-container" />
      );
    }
  });

  React.render(<AppContainer />, document.body);

});