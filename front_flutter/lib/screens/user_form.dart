// lib/screens/user_form.dart



import 'package:flutter/material.dart';

import 'package:front_flutter/configuration/api_service.dart';

import 'package:front_flutter/models/user.dart';



class UserForm extends StatefulWidget {

  final Function onUserAdded;



  UserForm({required this.onUserAdded});



  @override

  _UserFormState createState() => _UserFormState();

}



class _UserFormState extends State<UserForm> {

  final nameController = TextEditingController();

  final emailController = TextEditingController();

  final phoneController = TextEditingController();



  Future<void> _submitForm() async {

    final name = nameController.text;

    final email = emailController.text;

    final phone = phoneController.text;





    if (name.isNotEmpty && email.isNotEmpty && phone.isNotEmpty) {

      final user = User(

        id: 0,

        name: name,

        email: email,

        phone: phone,

      );

      try {

// envia os dados para o backend

        await ApiService.createUser(user);

// atualiza a lista de usuários na tela anterior

        widget.onUserAdded();



// limpa os campos

        nameController.clear();

        emailController.clear();

        phoneController.clear();



// mostra que deu certo

        ScaffoldMessenger.of(context).showSnackBar(

          SnackBar(content: Text('Usuário cadastrado com sucesso!')),

        );

      } catch (error) {

        print('Erro ao criar usuário: $error');

// mostra que deu errado

        ScaffoldMessenger.of(context).showSnackBar(

          SnackBar(content: Text('Falha ao criar usuário. Tente novamente!')),

        );

      }

    } else {

// algum campo esteja vazio

      ScaffoldMessenger.of(context).showSnackBar(

        SnackBar(content: Text('Por favor, preencha todos os campos!')),

      );

    }

  }



  @override

  Widget build(BuildContext context) {

    return Column(

      children: [

        TextField(

          controller: nameController,

          decoration: InputDecoration(

            labelText: 'Nome',

            border: OutlineInputBorder(

              borderRadius: BorderRadius.circular(10),

            ),

            focusedBorder: OutlineInputBorder(

              borderRadius: BorderRadius.circular(10),

              borderSide: BorderSide(color: Colors.teal, width: 2),

            ),

            prefixIcon: Icon(Icons.person),

          ),

        ),

        SizedBox(height: 10),

        TextField(

          controller: emailController,

          decoration: InputDecoration(

            labelText: 'Email',

            border: OutlineInputBorder(

              borderRadius: BorderRadius.circular(10),

            ),

            focusedBorder: OutlineInputBorder(

              borderRadius: BorderRadius.circular(10),

              borderSide: BorderSide(color: Colors.teal, width: 2),

            ),

            prefixIcon: Icon(Icons.email),

          ),

        ),

        SizedBox(height: 10),

        TextField(

          controller: phoneController,

          decoration: InputDecoration(

            labelText: 'Telefone',

            border: OutlineInputBorder(

              borderRadius: BorderRadius.circular(10),

            ),

            focusedBorder: OutlineInputBorder(

              borderRadius: BorderRadius.circular(10),

              borderSide: BorderSide(color: Colors.teal, width: 2),

            ),

            prefixIcon: Icon(Icons.phone),

          ),

        ),

        SizedBox(height: 20),

        ElevatedButton(

          onPressed: _submitForm,

          style: ElevatedButton.styleFrom(

            backgroundColor: Colors.teal,

            padding: EdgeInsets.symmetric(vertical: 16),

            shape: RoundedRectangleBorder(

              borderRadius: BorderRadius.circular(10),

            ),

          ),

          child: Text(

            'Cadastrar',

            style: TextStyle(fontSize: 16),

          ),

        ),

      ],

    );

  }

}

// uma coisa que vi e que em versoes anteriores ao flutter para mudar cor
//precisava primary porem em versoes nova tem que coloca backgroundcolor
// tive 4 erros por conta disso comentarioa penas para fins de informção

