import Image from "next/image";
import { Card } from "../components/card";

type Props = {
  title: string;
  description: string;
}

function ExampleComponent(props: Props) {
  return( 
    <div style={{backgroundColor: "#f9c0b0"}}>
      <h1>{props.title}</h1>
      <p>{props.description}</p>
    </div>
  )
}

export default function Home() {
  return (
    <div>
    <ExampleComponent title="Hello" description="Hello world component"></ExampleComponent>
    <ExampleComponent title="this is a different title" description="description"></ExampleComponent>
    <Card title="Card Title" description="Card Description" image="/next.svg"></Card>
    </div>
  );
}
