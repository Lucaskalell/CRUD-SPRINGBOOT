package com.vox.crud.Repository;

import com.vox.crud.MODEL.Users;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<Users, Long> {
}
// aqui nao preciso realizar nada de mudança prorio jpa vem com metodos basicos
// unica importação e do users para interação