<?php

namespace App\Controller;

use App\Entity\Device;
use App\Entity\User;
use App\Model\DeviceDto;
use App\Service\DeviceService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;
use Symfony\Component\Routing\Attribute\Route;

class DeviceController extends AbstractController
{
    public function __construct(private readonly DeviceService $deviceService)
    {}

    #[Route('/api/v1/devices/{user}', name: 'app_devices', methods: ['GET'], format: 'json', stateless: true)]
    public function index(User $user): JsonResponse
    {
        return $this->json($this->deviceService->getDevices(user: $user), Response::HTTP_OK, [], [
            'groups' => ['user'],
        ]);
    }

    #[Route('/api/v1/device/{mac}', name: 'app_device_mac', methods: ['GET'], format: 'json', stateless: true)]
    public function get_device_by_mac(Device $device): JsonResponse
    {
        return $this->json($device, Response::HTTP_OK, [], [
            'groups' => ['user'],
        ]);
    }

    #[Route('/api/v1/devices/{user}', name: 'app_device_create', methods: ['POST'])]
    public function create(#[MapRequestPayload] DeviceDto $device, User $user): JsonResponse
    {
        $this->deviceService->create(model: $device, user: $user);
        return $this->json([], Response::HTTP_CREATED, [], ['groups' => ['user']]);
    }
}