// lib/models/user.dart



class User {

  final int id;

  final String name;

  final String email;

  final String phone;



  User({

    required this.id,

    required this.name,

    required this.email,

    required this.phone,

  });



  factory User.fromJson(Map<String, dynamic> json) {

    return User(

      id: json['id'] ?? 0, // como tive dificuldades com flutter coloquei zero pra evita  nulos

      name: json['name'] ?? '',

      email: json['email'] ?? '',

      phone: json['phone'] ?? '',

    );

  }



  Map<String, dynamic> toJson() {

    return {

      'name': name,

      'email': email,

      'phone': phone,

    };

  }

}





