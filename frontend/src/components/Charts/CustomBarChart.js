import { useMemo } from "react";
import {
      BarChart,
      Bar,
      XAxis,
      YAxis,
      CartesianGrid,
      Tooltip,
      Legend,
      ReferenceLine,
      Text,
      ResponsiveContainer
} from "recharts";

const data = [
      {
            name: "Active / Reflective",
            uv: -2200,
            pv: -9000,
            amt: -1000
      },
      {
            name: "Sensing / Intuitive",
            uv: 6000,
            pv: 5000,
            amt: 4000
      },
      {
            name: "Visual / Verbal",
            uv: -2000,
            pv: -9800,
            amt: -400
      },
      {
            name: "Sequential / Global",
            uv: -4000,
            pv: 3000,
            amt: 550
      }
];


export default function CustomBarChart() {

      return (
            <ResponsiveContainer height={60 * data.length} debounce={50} style={{ margin: '20px' }}>

                  <BarChart
                        layout="vertical"
                        data={data}
                        stackOffset="sign"
                        barGap="0"
                        barSize={30}
                  >
                        <XAxis hide type="number" />
                        <YAxis
                              orientation="left"
                              dataKey="name"
                              type="category"
                              axisLine={false}
                              tickLine={false}
                        />
                        <Tooltip />
                        <Legend />
                        <ReferenceLine y={0} stroke="#000" />
                        <Bar name="ILS" dataKey="pv" fill="#8884d8" />
                        <Bar name="KI" dataKey="uv" fill="#82ca9d" />
                        <Bar name="Übungen" dataKey="amt" fill="#30588e" />
                  </BarChart>
            </ResponsiveContainer>);
};