// tela principal utilizando conceito basico do crud Criar,Read(ler),update(atualiza),Delete(excluir)
import { useState, useEffect } from "react";
import './style.css';
import api from '../../Services/api.js';

function Home() {
    const [users, setUsers] = useState([]);
    const [message, setMessage] = useState("");
    const [editingUser, setEditingUser] = useState(null);

    // função para buscar os usuários
    async function getUsers() {
        try {
            const response = await api.get("/users");
            setUsers(response.data);
        } catch {
            setMessage("Erro ao carregar usuários. Tente novamente.");
        }
    }

    // função para cadastrar ou atualizar
    async function handleSubmit(e) {
        e.preventDefault();
        const name = e.target.name.value;
        const email = e.target.email.value;
        const telefone = e.target.telefone.value;

        if (editingUser) {
            // atualiza  usuário
            try {
                await api.put(`/users/${editingUser.id}`, { name, email, telefone });
                setMessage("Usuário atualizado com sucesso!");
                setEditingUser(null); // limpa a edição
                getUsers(); // atualiza a lista
            } catch {
                setMessage("Erro ao atualizar usuário. Tente novamente.");
            }
        } else {
            // cadastrar  usuário
            try {
                await api.post("/users", { name, email, telefone });
                setMessage("Usuário cadastrado com sucesso!");
                getUsers();
            } catch {
                setMessage("Erro ao cadastrar usuário. Tente novamente.");
            }
        }
    }

    // função pra apagar o  usuário
    async function handleDelete(userId) {
        try {
            await api.delete(`/users/${userId}`);
            setMessage("Usuário excluído com sucesso!");
            getUsers();
        } catch {
            setMessage("Erro ao excluir usuário. Tente novamente.");
        }
    }

    //  iniciar a edição
    function handleEdit(user) {
        setEditingUser(user);
    }

    // carrega os usuários
    useEffect(() => {
        getUsers();
    }, []);

    return (
        <div className="container">
            <form onSubmit={handleSubmit}>
                <h1>{editingUser ? "Editar usuário" : "Cadastro de usuários"}</h1>
                <input
                    placeholder="Nome"
                    name="name"
                    type="text"
                    defaultValue={editingUser?.name || ""}
                    required
                />
                <input
                    placeholder="Email"
                    name="email"
                    type="email"
                    defaultValue={editingUser?.email || ""}
                    required
                />
                <input
                    placeholder="Telefone"
                    name="telefone"
                    type="text"
                    defaultValue={editingUser?.telefone || ""}
                    required
                />
                <button type="submit">
                    {editingUser ? "Atualizar" : "Cadastrar"}
                </button>
                {editingUser && (
                    <button
                        type="button"
                        onClick={() => setEditingUser(null)}
                        className="cancel-btn"
                    >
                        Cancelar
                    </button>
                )}
            </form>

            {message && <p>{message}</p>}

            <div>
                <h2>Usuários Cadastrados</h2>
                <ul>
                    {users.map((user) => (
                        <li key={user.id}>
                            {user.name} - {user.email} - {user.telefone}
                            <button onClick={() => handleEdit(user)} className="edit-btn">
                                Editar
                            </button>
                            <button onClick={() => handleDelete(user.id)} className="delete-btn">
                                Excluir
                            </button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Home;





