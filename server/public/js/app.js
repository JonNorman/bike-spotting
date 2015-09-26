
$(document).ready(function () {

  var AppContainer = React.createClass({

    render: function() {
      return (
        <div className="app-container">
          <SideBar />
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

  var SideBar = React.createClass({
    render: function() {
      return (
        <div className="sidebar">
          <div className="sidebar-heading">
            <a href="/">
              <i className="fa fa-2x fa-binoculars"></i>
              <br />
              <h1>Bike Spotting</h1>
            </a>
          </div>
          <div className="sidebar-description">
            <p>This is some explanation of the site</p>
          </div>
          <div className="sidebar-footer">
            <p>This is where you give links to collaborators, @Twitter, #GitHub etc.</p>
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

      var biggestStation = 0;
      Object.keys(this.state.data).forEach(function (k) {
        var d = _this.state.data[k];

        if (parseInt(d.nbDocks) > biggestStation) {
          biggestStation = d.nbDocks;
        }
      })

      Object.keys(this.state.data).forEach(function (k) {
        var d = _this.state.data[k];

        var markerScalar = 16 * (d.nbDocks/biggestStation)
        var strokeColor = "#2c3e50";
        var fillColor = "#e74c3c";
        var strokeWeight = 2;

        var marker = new google.maps.Marker({
          position: { lat: parseFloat(d.lat), lng: parseFloat(d.long) },
          map: _this.state.map,
          title: 'Hello World!',
          icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: markerScalar,
            strokeWeight: strokeWeight,
            strokeColor: strokeColor,
            fillColor: fillColor,
            fillOpacity: 1-(d.nbEmptyDocks/d.nbDocks)
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