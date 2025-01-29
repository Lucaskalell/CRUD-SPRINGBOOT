// lib/screens/home_screen.dart



import 'package:flutter/material.dart';

import 'package:front_flutter/configuration/api_service.dart';

import 'package:front_flutter/models/user.dart';

import 'package:front_flutter/screens/user_form.dart';



class HomeScreen extends StatefulWidget {

  @override

  _HomeScreenState createState() => _HomeScreenState();

}



class _HomeScreenState extends State<HomeScreen> {

  List<User> users = [];



  @override

  void initState() {

    super.initState();

    _fetchUsers();

  }





  Future<void> _fetchUsers() async {

    try {

      final fetchedUsers = await ApiService.fetchUsers();

      setState(() {

        users = fetchedUsers;

      });

    } catch (error) {

      print('Erro ao carregar usuários: $error');

    }

  }



// Deletar usuário

  Future<void> _deleteUser(int id) async {

    try {

      await ApiService.deleteUser(id);

      _fetchUsers(); // atualiza a lista de usuários

    } catch (error) {

      print('Erro ao deletar usuário: $error');

    }

  }



// chama a função para adicionar um usuário

  void _onUserAdded() {

    _fetchUsers();

  }



  @override

  Widget build(BuildContext context) {

    return Scaffold(

      appBar: AppBar(

        title: Text('Cadastro de Usuários'),

        backgroundColor: Colors.teal, // muda cor da tela principal

      ),

      body: Padding(

        padding: const EdgeInsets.all(16.0),

        child: Column(

          crossAxisAlignment: CrossAxisAlignment.start,

          children: [

// formulário de cadastro

            Container(

              padding: EdgeInsets.all(16),

              decoration: BoxDecoration(

                color: Colors.white,

                borderRadius: BorderRadius.circular(8),

                boxShadow: [

                  BoxShadow(

                    color: Colors.black.withOpacity(0.1),

                    blurRadius: 6,

                    offset: Offset(0, 3),

                  ),

                ],

              ),

              child: UserForm(onUserAdded: _onUserAdded),

            ),

            SizedBox(height: 20),



            Expanded(

              child: ListView.builder(

                itemCount: users.length,

                itemBuilder: (context, index) {

                  return Card(

                    margin: EdgeInsets.symmetric(vertical: 8),

                    shape: RoundedRectangleBorder(

                      borderRadius: BorderRadius.circular(10),

                    ),

                    elevation: 5,

                    child: ListTile(

                      contentPadding: EdgeInsets.all(16),

                      title: Text(

                        users[index].name,

                        style: TextStyle(fontWeight: FontWeight.bold),

                      ),

                      subtitle: Column(

                        crossAxisAlignment: CrossAxisAlignment.start,

                        children: [

                          Text(users[index].email),

                          Text(users[index].phone),

                        ],

                      ),// botao da lixeira

                      trailing: IconButton(

                        icon: Icon(Icons.delete, color: Colors.red),

                        onPressed: () => _deleteUser(users[index].id),

                      ),

                    ),

                  );

                },

              ),

            ),

          ],

        ),

      ),

    );

  }

}


