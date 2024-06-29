<?php

namespace App\Service;

use App\Repository\UserRepository;

readonly class UserService
{
    public function __construct(private UserRepository $userRepository)
    {}

    public function getUserById(string $id)
    {
        return $this->userRepository->find($id);
    }

    public function getUsers(): array
    {
        return $this->userRepository->findAll();
    }
}