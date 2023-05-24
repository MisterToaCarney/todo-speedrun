<script lang="ts">
    import { getDocs, doc, collection, query, addDoc, onSnapshot, deleteDoc, setDoc } from "firebase/firestore"
    import { db } from "../lib/my_firebase"
    import { onDestroy } from "svelte";

    console.log(db);

    const q = query(collection(db, "/todos"))
    
    const unsubscribe = onSnapshot(q, querySnapshot => {
        todos = []
        querySnapshot.forEach(doc => {
            todos.push({
                id: doc.id,
                text: doc.data().text,
                completed: doc.data().completed
            })
        })
        todos = todos
    })


    // Types
    interface TodoEntry {
        id: string
        text: string
        completed: boolean
    }

    // State
    let todos: Array<TodoEntry> = []
    let inputValue = "";

    // functions
    function addTodo(text: string) {
        const ref = collection(db, "/todos")

        addDoc(ref, {
            text: text,
            completed: false
        })

        inputValue = "";
    }
    function removeTodo(id: string) {
        const ref = doc(db, "/todos", id)
        deleteDoc(ref)
    }
    function updateTodo(id: string, newTodo: TodoEntry) {
        console.log(newTodo);
        
        const ref = doc(db, "/todos", id)
        setDoc(ref, {
            text: newTodo.text,
            completed: newTodo.completed
        })
    }
    
    onDestroy(unsubscribe)

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
                <th class="w-0">ID</th>
                <th>Todo</th>
                <th class="w-0"></th>
            </tr>
          </thead>
          <tbody>
            {#each todos as todo, i}
                <tr>
                    <td class=""><input type="checkbox" class="checkbox align-middle" bind:checked={todo.completed} on:change={e => updateTodo(todo.id, {...todo})}></td>
                    <td class="">{i+1}</td>
                    <td>{todo.id}</td>
                    <td>{todo.text}</td>
                    <td><button on:click={e => removeTodo(todo.id)} class="btn btn-error">Remove</button></td>
                </tr>
            {/each}
          </tbody>
        </table>
      </div>
</main>

