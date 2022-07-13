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
            uv: 4000,
            pv: 3000,
            amt: 550
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
                        barGap="0"
                        barSize={30}
                  >
                        {/* <CartesianGrid strokeDasharray="3 3" /> */}
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