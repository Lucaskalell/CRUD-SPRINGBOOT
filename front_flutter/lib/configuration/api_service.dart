import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:front_flutter/models/user.dart';



class ApiService {

  static const String baseUrl = 'http://localhost:8080/api';



// busca todos os usuários

  static Future<List<User>> fetchUsers() async {

    final response = await http.get(Uri.parse(baseUrl + '/users'));

    if (response.statusCode == 200) {

      final List<dynamic> data = jsonDecode(response.body);

      return data.map((json) => User.fromJson(json)).toList();

    } else {

      throw Exception('Falha ao carregar usuários: ${response.statusCode}');

    }

  }



// cria um novo usuário

  static Future<void> createUser(User user) async {

    final response = await http.post(

      Uri.parse(baseUrl + '/users'),

      headers: {'Content-Type': 'application/json'},

      body: jsonEncode({

        'name': user.name,

        'email': user.email,

        'phone': user.phone,

      }),

    );



    if (response.statusCode == 200 || response.statusCode == 201) {

      print("Usuário criado com sucesso: ${response.body}");

    } else {

      throw Exception('Falha ao criar usuário: ${response.statusCode}');

    }

  }



// apaga um usuário pelo ID

  static Future<void> deleteUser(int id) async {

    final response = await http.delete(Uri.parse(baseUrl + '/users/$id'));



    if (response.statusCode == 200) {

      print("Usuário deletado com sucesso: ID $id");

    } else if (response.statusCode == 404) {

      throw Exception('Usuário não encontrado: ID $id');

    } else {

      throw Exception('Falha ao deletar usuário: ${response.statusCode}');

    }

  }

}

