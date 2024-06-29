<?php

namespace App\Controller;

use App\Service\UserService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class UserController extends AbstractController
{
    public function __construct(private readonly UserService $userService)
    {}

    #[Route('/api/v1/users', name: 'app_users', methods: ['GET'])]
    public function index(): JsonResponse
    {
        return $this->json($this->userService->getUsers(), Response::HTTP_OK, [], [
            'groups' => ['user'],
        ]);
    }
}