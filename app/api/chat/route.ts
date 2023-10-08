import { NextRequest } from 'next/server';
import { Message as VercelChatMessage, StreamingTextResponse } from 'ai';
import { ChatOpenAI } from 'langchain/chat_models/openai';
import { BytesOutputParser } from 'langchain/schema/output_parser';
import { PromptTemplate } from 'langchain/prompts';
export const runtime = 'edge';

const formatMessage = (message: VercelChatMessage) => {
    return `${message.role}: ${message.content}`;
};

const TEMPLATE = `
Rules:
{rules}

Adjacent Hexes:
{adjacent}

Hex Details:
{details}

Current conversation:
{chat_history}
 
User: {input}
AI:`;

export async function POST(req: NextRequest) {
    const body = await req.json();
    const details = body.details
    const adjacent = body.adjacent
    const messages = body.messages ?? [];
    const formattedPreviousMessages = messages.slice(0, -1).map(formatMessage);
    const currentMessageContent = messages[messages.length - 1].content;

    const prompt = PromptTemplate.fromTemplate(TEMPLATE);

    const model = new ChatOpenAI({
        modelName: "gpt-4",
        temperature: 0.3,
    });

    const outputParser = new BytesOutputParser();
    const chain = prompt.pipe(model).pipe(outputParser);

    let ruleSet = `As a creative DM's assistant who loves to roll with strange scenarios, 
    please try your best to weave an interesting narrative based on the current Hex's information combined 
    with the adjacent Hexes' information (hexes have pointy end on top). Be descriptive and assertive.`

    const stream = await chain.stream({
        rules: ruleSet,
        adjacent: adjacent,
        details: details,
        chat_history: formattedPreviousMessages.join('\n'),
        input: currentMessageContent,
    });

    return new StreamingTextResponse(stream);
}