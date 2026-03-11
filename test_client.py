{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "978bbbb4-a84d-4329-8534-6ad49062b977",
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "asyncio.run() cannot be called from a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 24\u001b[0m\n\u001b[0;32m     21\u001b[0m         task_list \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mawait\u001b[39;00m client\u001b[38;5;241m.\u001b[39mread_resource(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtasks://all\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     22\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124mAll tasks:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m, task_list\u001b[38;5;241m.\u001b[39mcontents[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m.\u001b[39mtext)\n\u001b[1;32m---> 24\u001b[0m asyncio\u001b[38;5;241m.\u001b[39mrun(test_server())\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\asyncio\\runners.py:191\u001b[0m, in \u001b[0;36mrun\u001b[1;34m(main, debug, loop_factory)\u001b[0m\n\u001b[0;32m    161\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Execute the coroutine and return the result.\u001b[39;00m\n\u001b[0;32m    162\u001b[0m \n\u001b[0;32m    163\u001b[0m \u001b[38;5;124;03mThis function runs the passed coroutine, taking care of\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    187\u001b[0m \u001b[38;5;124;03m    asyncio.run(main())\u001b[39;00m\n\u001b[0;32m    188\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    189\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    190\u001b[0m     \u001b[38;5;66;03m# fail fast with short traceback\u001b[39;00m\n\u001b[1;32m--> 191\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[0;32m    192\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124masyncio.run() cannot be called from a running event loop\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    194\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m Runner(debug\u001b[38;5;241m=\u001b[39mdebug, loop_factory\u001b[38;5;241m=\u001b[39mloop_factory) \u001b[38;5;28;01mas\u001b[39;00m runner:\n\u001b[0;32m    195\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m runner\u001b[38;5;241m.\u001b[39mrun(main)\n",
      "\u001b[1;31mRuntimeError\u001b[0m: asyncio.run() cannot be called from a running event loop"
     ]
    }
   ],
   "source": [
    "from fastmcp import Client\n",
    "import asyncio\n",
    " \n",
    "async def test_server():\n",
    "    async with Client(\"task_server.py\") as client:\n",
    "        # List available tools\n",
    "        tools = await client.list_tools()\n",
    "        print(\"Available tools:\", [t.name for t in tools.tools])\n",
    "        \n",
    "        # Add a task\n",
    "        result = await client.call_tool(\"add_task\", {\n",
    "            \"title\": \"Learn MCP\",\n",
    "            \"description\": \"Build a task tracker with FastMCP\"\n",
    "        })\n",
    "        print(\"\\nAdded task:\", result.content[0].text)\n",
    "        \n",
    "        # View all tasks\n",
    "        resources = await client.list_resources()\n",
    "        print(\"\\nAvailable resources:\", [r.uri for r in resources.resources])\n",
    "        \n",
    "        task_list = await client.read_resource(\"tasks://all\")\n",
    "        print(\"\\nAll tasks:\\n\", task_list.contents[0].text)\n",
    " \n",
    "asyncio.run(test_server())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e9af3c14-b533-4720-aebb-ff284e89082b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Unsupported script type: task_server.ipynb",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 30\u001b[0m\n\u001b[0;32m     27\u001b[0m             \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124mAll tasks:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m, task_list\u001b[38;5;241m.\u001b[39mcontents[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m.\u001b[39mtext)\n\u001b[0;32m     29\u001b[0m \u001b[38;5;66;03m# Call it directly without asyncio.run()\u001b[39;00m\n\u001b[1;32m---> 30\u001b[0m \u001b[38;5;28;01mawait\u001b[39;00m test_server()\n",
      "Cell \u001b[1;32mIn[4], line 3\u001b[0m, in \u001b[0;36mtest_server\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01masync\u001b[39;00m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mtest_server\u001b[39m():\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;66;03m# ... your client setup code ...\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m     \u001b[38;5;28;01masync\u001b[39;00m \u001b[38;5;28;01mwith\u001b[39;00m Client(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtask_server.ipynb\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m client:\n\u001b[0;32m      4\u001b[0m         \u001b[38;5;66;03m# List available tools\u001b[39;00m\n\u001b[0;32m      5\u001b[0m         tools \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mawait\u001b[39;00m client\u001b[38;5;241m.\u001b[39mlist_tools()\n\u001b[0;32m      6\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAvailable tools:\u001b[39m\u001b[38;5;124m\"\u001b[39m, [t\u001b[38;5;241m.\u001b[39mname \u001b[38;5;28;01mfor\u001b[39;00m t \u001b[38;5;129;01min\u001b[39;00m tools\u001b[38;5;241m.\u001b[39mtools])\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\fastmcp\\client\\client.py:264\u001b[0m, in \u001b[0;36mClient.__init__\u001b[1;34m(self, transport, name, roots, sampling_handler, sampling_capabilities, elicitation_handler, log_handler, message_handler, progress_handler, timeout, auto_initialize, init_timeout, client_info, auth)\u001b[0m\n\u001b[0;32m    236\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m__init__\u001b[39m(\n\u001b[0;32m    237\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[0;32m    238\u001b[0m     transport: (\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    260\u001b[0m     auth: httpx\u001b[38;5;241m.\u001b[39mAuth \u001b[38;5;241m|\u001b[39m Literal[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moauth\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m|\u001b[39m \u001b[38;5;28mstr\u001b[39m \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[0;32m    261\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    262\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mname \u001b[38;5;241m=\u001b[39m name \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mgenerate_name()\n\u001b[1;32m--> 264\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtransport \u001b[38;5;241m=\u001b[39m cast(ClientTransportT, infer_transport(transport))\n\u001b[0;32m    265\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m auth \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    266\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtransport\u001b[38;5;241m.\u001b[39m_set_auth(auth)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\fastmcp\\client\\transports\\inference.py:129\u001b[0m, in \u001b[0;36minfer_transport\u001b[1;34m(transport)\u001b[0m\n\u001b[0;32m    127\u001b[0m         inferred_transport \u001b[38;5;241m=\u001b[39m NodeStdioTransport(script_path\u001b[38;5;241m=\u001b[39mcast(Path, transport))\n\u001b[0;32m    128\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m--> 129\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mUnsupported script type: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mtransport\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    131\u001b[0m \u001b[38;5;66;03m# the transport is an http(s) URL\u001b[39;00m\n\u001b[0;32m    132\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(transport, AnyUrl \u001b[38;5;241m|\u001b[39m \u001b[38;5;28mstr\u001b[39m) \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(transport)\u001b[38;5;241m.\u001b[39mstartswith(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhttp\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n",
      "\u001b[1;31mValueError\u001b[0m: Unsupported script type: task_server.ipynb"
     ]
    }
   ],
   "source": [
    "async def test_server():\n",
    "    # ... your client setup code ...\n",
    "    async with Client(\"task_server.py\") as client:\n",
    "        # List available tools\n",
    "        tools = await client.list_tools()\n",
    "        print(\"Available tools:\", [t.name for t in tools.tools])\n",
    "        \n",
    "        # Add a task\n",
    "        result = await client.call_tool(\"add_task\", {\n",
    "            \"title\": \"Learn MCP\",\n",
    "            \"description\": \"Build a task tracker with FastMCP\"\n",
    "        })\n",
    "        print(\"\\nAdded task:\", result.content[0].text)\n",
    "        \n",
    "        # View all tasks\n",
    "        resources = await client.list_resources()\n",
    "        print(\"\\nAvailable resources:\", [r.uri for r in resources.resources])\n",
    "        \n",
    "        task_list = await client.read_resource(\"tasks://all\")\n",
    "        print(\"\\nAll tasks:\\n\", task_list.contents[0].text)\n",
    "    async with stdio_client(server_params) as (read, write):\n",
    "        async with ClientSession(read, write) as client:\n",
    "            await client.initialize()\n",
    "            \n",
    "            # Example: Reading a resource\n",
    "            task_list = await client.read_resource(\"tasks://all\")\n",
    "            print(\"\\nAll tasks:\\n\", task_list.contents[0].text)\n",
    "\n",
    "# Call it directly without asyncio.run()\n",
    "await test_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "dfb829c2-6db0-4f13-9c05-0e594185437a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
