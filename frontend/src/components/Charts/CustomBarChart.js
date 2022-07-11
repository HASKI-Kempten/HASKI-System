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
            uv: -1200,
            pv: -9000,
            amt: 2000
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
            amt: 2290
      },
      {
            name: "Sequential / Global",
            uv: 2780,
            pv: 300,
            amt: 100
      }
];
const YAxisLeftTick = ({ y, payload: { value } }) => {
      return (
            <Text x={0} y={y} textAnchor="start" verticalAnchor="middle" scaleToFit>
                  {value}
            </Text>
      );
};
let ctx;
export const measureText14HelveticaNeue = text => {
      if (!ctx) {
            ctx = document.createElement("canvas").getContext("2d");
            ctx.font = "14px 'Helvetica Neue";
      }

      return ctx.measureText(text).width;
};
const BAR_AXIS_SPACE = 10;

export default function CustomBarChart() {
      const maxTextWidth = useMemo(
            () =>
                  data.reduce((acc, cur) => {
                        const value = cur["name"];
                        const width = measureText14HelveticaNeue(value.toLocaleString());
                        if (width > acc) {
                              return width;
                        }
                        return acc;
                  }, 0),
            []
      );
      return (
            <ResponsiveContainer height={60 * data.length} debounce={50} style={{ margin: '20px' }}>

                  <BarChart
                        layout="vertical"
                        data={data}
                        stackOffset="sign"
                        margin={{ left: 10, right: 10 }}
                  >
                        {/* <CartesianGrid strokeDasharray="3 3" /> */}
                        <XAxis hide type="number" />
                        <YAxis
                              orientation="left"
                              dataKey="name"
                              type="category"
                              axisLine={false}
                              tickLine={false}
                              mirror
                        />
                        <Tooltip />
                        <Legend />
                        <ReferenceLine y={0} stroke="#000" />
                        <Bar name="List" dataKey="pv" fill="#8884d8" stackId="stack" />
                        <Bar name="KI" dataKey="uv" fill="#82ca9d" stackId="stack" />
                        <Bar name="Übungen" dataKey="amt" fill="#30588e" stackId="stack" />
                  </BarChart>
            </ResponsiveContainer>);
};