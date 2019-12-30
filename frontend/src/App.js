import React from 'react';
import { LineChart, Line, Tooltip, XAxis, YAxis } from 'recharts';
import './App.css';

const getLocalDate = dateStrFromApi => {
    // add utc indicator to date
    return new Date(`${dateStrFromApi}Z`)
}

const CustomTooltip = ({active, payload, label}) => {
    if (active) {
        const data = payload[0].payload
        return (<div className="custom-tooltip">
            <p className="label"><a href={`http://twitter.com/meganamram/status/${data.id}`}>Tweet</a></p>
            <p className="label">Retweets: {data.retweets}</p>
            <p className="label">Likes: {data.likes}</p>
            <p className="label">Date: {data.date.toString()}</p>
        </div>)
    }
    return null
}

class Chart extends React.Component {
    dataForChart() {
        return this.props.data
            .filter(tweet => tweet.date)
            .map(tweet => {
                return { id: tweet.tweet_id, retweets: tweet.retweets, likes: tweet.likes, date: getLocalDate(tweet.date) }
            })
    }

    render() {
        const data = this.dataForChart()
        data.reverse()
        return <LineChart width={1200} height={600} data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
            <Line dataKey="retweets" type="natural" stroke="#82ca9d" />
            <XAxis dataKey="date" />
            <YAxis scale="log" domain={['auto', 'auto']} />
            <Tooltip content={<CustomTooltip />} />
        </LineChart>
    }
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            loading: true,
            error: false,
            all: [],
            topByRetweets: [],
            topByLikes: [],
        }
    }

    componentDidMount() {
        let url = "http://api.todaywasthedaydonaldtrumpfinallybecamepresident.com"
        if (window.location.hostname === "localhost") {
            url = "http://localhost:5000"
        }
        fetch(url)
            .then(resp => resp.json())
            .then(json => {
                this.setState({
                    loading: false,
                    all: json.all,
                    topByLikes: json.top_by_likes,
                    topByRetweets: json.topByRetweets
                })
            })
            .catch(() => this.setState({ loading: false, error: true }))
    }

    render() {
        if (this.state.loading) {
            return "Loading..."
        } else if (this.state.error) {
            return "Error!"
        } else {
            return <Chart data={this.state.all}/>
        }
    }
}

export default App;
