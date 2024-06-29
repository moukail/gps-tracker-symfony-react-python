<?php

namespace App\Controller;

use App\Entity\Device;
use App\Model\LocationDto;
use App\Service\LocationService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;
use Symfony\Component\Routing\Attribute\Route;

class LocationController extends AbstractController
{
    public function __construct(private readonly LocationService $locationService)
    {}

    #[Route('/api/v1/locations/{device}', name: 'app_locations', methods: ['GET'])]
    public function index(Device $device): JsonResponse
    {
        return $this->json($this->locationService->getLocations(device: $device), Response::HTTP_OK, [], [
            'groups' => ['user'],
        ]);
    }

    #[Route('/api/v1/locations/{device}', name: 'app_location_create', methods: ['POST'])]
    public function create(#[MapRequestPayload] LocationDto $location, Device $device): JsonResponse
    {
        $this->locationService->create(model: $location, device: $device);
        return $this->json([], Response::HTTP_CREATED, [], ['groups' => ['user']]);
    }
}