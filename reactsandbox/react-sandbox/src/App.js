import React, { Component } from 'react';

// 引入 ECharts 主模块
import echarts from 'echarts/lib/echarts';
// 引入柱状图
import  'echarts/lib/chart/line';
import  'echarts/lib/chart/bar';
// 引入提示框和标题组件
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';


class App extends Component {
    constructor(props) {
    // Need to remember to call the parent constructor.
      super(props)

    // We create a state object and set our initial state in it
      this.state={
            type:"line",
            data:[ ],
            seriesData:[ ]
        };
        this.initBarEcharts  = this.initBarEcharts.bind(this);
  }

    initBarEcharts(){
        let myChart = echarts.init(document.getElementById('main'));
        let options = this.state.type === "bar" ? {
            title: { text: 'ECharts' },
            tooltip: {},
            xAxis: {
                name: 'Year',
                data: this.state.data
            },
            yAxis: {},
            series: [{
                name: 'Temp',
                type: 'bar',
                smooth: true,
                data: this.state.seriesData
            }]
        } :{
            title: { text: 'ECharts' },
            tooltip: {},
            xAxis: {
                name: 'Year',
                data: this.state.data
            },
            yAxis: {},
            series: [{
                name: 'Temp',
                type: 'line',
                smooth: true,
                data: this.state.seriesData
            }]
        };
        myChart.setOption(options,true)
    }
    componentDidMount() {
        this.initBarEcharts();
    }
    componentWillUpdate(){

    }
    componentDidUpdate(){
        this.initBarEcharts();
    }
    increment = () => {
      const getUrl = '/formats/'
      fetch(getUrl)
      .then(response => {
        console.log(response.json)
        // Convert the response to JSON
        const a = response.json()
        return  a
      })
      .then(data => {
        const xdata = []
        const ydata = []
        if (data.length > 99) {
          for (let i = 0; i < 99; i++ ) {
            xdata.push(data[i].Year)
            ydata.push(data[i].Temp)
          }
        }
        xdata.reverse()
        ydata.reverse()
        console.log('%c HTTP GET Response:', 'color: #f542e6')
        console.log(data)
        console.log(xdata)
        console.log(ydata)
        this.setState({
        data: xdata,
        seriesData: ydata,
    })
      })
    }
    setType = (type) => {
        this.setState({type})
    }
    render() {
        return (
            <div>
              <button style={{color: "#ff0000"}} className="mybuttoncolor" onClick={this.increment}>get data</button>
              <button style={{color: "#0000ff"}} className="mybuttoncolor" onClick={()=>this.setType("bar")}>Bar</button>
              <button style={{color: "#00ff00"}} className="mybuttoncolor" onClick={()=>this.setType("line")}>Line</button>
              <div id="main" style={{ width: 800, height: 600 }}></div>
            </div>
        );
    }
}

export default App;