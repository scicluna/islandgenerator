import type { Island } from "@/types/islandTypes";
import World from "@/components/World";
import { readJsonChunks } from "@/utils/readJsonChunks";


export default async function Main() {
  const islandChain: Island[][] = await readJsonChunks();
  console.log("chunks", islandChain.length)

  return (
    <main className="w-fit h-fit">
      <World islandChain={islandChain} />
    </main>
  )
}
