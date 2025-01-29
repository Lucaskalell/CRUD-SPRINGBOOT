import 'package:http/http.dart' as http;
import 'package:meu_app_flutter/models/user.dart';

class ApiService {
  static const String baseUrl = 'http://localhost:8080/api';

  static Future<List<User>> fetchUsers() async {
    final response = await http.get(Uri.parse(baseUrl));
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((json) => User.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load users');
    }
  }
}