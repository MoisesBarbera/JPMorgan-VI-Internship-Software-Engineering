// Moises Barbera Ramos - 17 / 11 / 2019

import React, { Component } from 'react';
import { Table } from '@jpmorganchase/perspective';
import { ServerRespond } from './DataStreamer';
import { DataManipulator } from './DataManipulator';
import './Graph.css';

interface IProps {
  data: ServerRespond[],
}

interface PerspectiveViewerElement extends HTMLElement {
  load: (table: Table) => void,
}
class Graph extends Component<IProps, {}> {
  table: Table | undefined;

  render() {
    return React.createElement('perspective-viewer');
  }

  componentDidMount() {
    // Get element from the DOM.
    const elem = document.getElementsByTagName('perspective-viewer')[0] as unknown as PerspectiveViewerElement;

    const schema = {
	  price_abc: 'float',    // the variable price_abc in this .tsx file is used as a number, referred to as float in react
	  price_def: 'float',    // the variable price_def in this .tsx file is used as a number, referred to as float in react
	  ratio: 'float',    // the variable ratio in this .tsx file is used as a number, referred to as float in react
	  timestamp: 'date',    // the variable timestamp in this .tsx file is used as a date
	  upper_bound: 'float',    // the variable upper_bound in this .tsx file is used as a number, referred to as float in react
	  lower_bound: 'float',    // the variable lower_bound in this .tsx file is used as a number, referred to as float in react
	  trigger_alert: 'float',    // the variable trigger_alert in this .tsx file is used as a number, referred to as float in react
    };

    if (window.perspective && window.perspective.worker()) {
      this.table = window.perspective.worker().table(schema);
    }
    if (this.table) {
      // Load the `table` in the `<perspective-viewer>` DOM reference.
      elem.load(this.table);
      elem.setAttribute('view', 'y_line');  // ‘view’ is the the kind of graph we wanted to visualize the data as, starting by setting it to y_line.
	  elem.setAttribute('row-pivots', '["timestamp"]');  // 'row-pivots' states the x-axis. Then we can map ach datapoint based on the timestamp it has.
      elem.setAttribute('columns', '["ratio", "lower_bound", "upper_bound", "trigger_alert"]');  // Focuses on a particular part of the datapoints along the y_axis so that the plot doesn't plot all fields and values of each datapoint. In thi case  we are only tracking: the ratio, the lower_bound, the upper_bound and the trigger_alert.

      elem.setAttribute('aggregates', JSON.stringify({  // here aggregates takes care of the dulicates of data for the price_abc, price_def, ratio, timestamp, upper_bound, lower_bound and the trigger_alert.
		  price_abc: 'avg',  // averages the price_abc values before treating it as one non-dupplicate value.
		  price_def: 'avg',  // averages the price_def values before treating it as one non-dupplicate value.
		  ratio: 'avg',  // averages the ratio values before treating it as one non-dupplicate value.
		  timestamp: 'distinct count',
		  upper_bound: 'avg',  // averages the upper_bound values before treating it as one non-dupplicate value.
		  lower_bound: 'avg',  // averages the lower_bound values before treating it as one non-dupplicate value.
		  trigger_alert: 'avg',  // averages the trigger_alert values before treating it as one non-dupplicate value.
      }));
    }
  }

  componentDidUpdate() {
    if (this.table) {
      this.table.update([  // here we added the open square bracket to enclose the DataManipulator.generateRow function which is described in the file DataManipulator.ts
        DataManipulator.generateRow(this.props.data),
      ]);  // finally I added here the closed square bracket enclosing the DataManipulator.generateRow function.
    }
  }
}

export default Graph;
