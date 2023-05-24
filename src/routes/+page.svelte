<script lang="ts">
    import { doc, setDoc, getDocs, collection, query } from "firebase/firestore"
    import { db } from "../lib/my_firebase"

    console.log(db);
    
    
    // Types
    interface TodoEntry {
        text: string
        completed: boolean
    }

    // State
    let todos: Array<TodoEntry> = []
    let inputValue = "";

    // functions
    function addTodo(text: string) {
        todos.push({
            text: text,
            completed: false
        });
        todos = todos;
        inputValue = "";
    }

    async function runQuery() {
        const q = query(collection(db, "/todos"))
        const querySnapshot = await getDocs(q)

        querySnapshot.forEach(document => {
            console.log(document.data());
        })
    }

    addTodo("test")
    runQuery()
</script>


<h1 class="text-center text-3xl my-4">My Todo App</h1>

<main class="px-8">

    <div class="flex gap-2 my-2">
        <input bind:value={inputValue} type="text" placeholder="Add Todo" class="input basis-full input-bordered " />
        <button class="btn btn-success" on:click={() => addTodo(inputValue)}>Add</button>
    </div>

    <div class="overflow-x-auto">
        <table class="table w-full">
          <!-- head -->
          <thead>
            <tr>
                <th class="w-0"></th>
                <th class="w-0"></th>
                <th>Todo</th>
                <th class="w-0"></th>
            </tr>
          </thead>
          <tbody>
            {#each todos as todo, i}
                <tr>
                    <td class=""><input type="checkbox" class="checkbox align-middle" bind:checked={todo.completed}></td>
                    <td class="">{i+1}</td>
                    <td>{todo.text}</td>
                    <td><button on:click={() => {todos.splice(i, 1); todos = todos}} class="btn btn-error">Remove</button></td>
                </tr>
            {/each}
          </tbody>
        </table>
      </div>

      <button class="btn" on:click={runQuery}>Okay</button>
</main>

