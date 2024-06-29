<?php

namespace App\Service;

use App\Entity\Device;
use App\Entity\User;
use App\Model\DeviceDto as Model;
use App\Repository\DeviceRepository;

readonly class DeviceService
{
    public function __construct(private DeviceRepository $deviceRepository) {}

    public function create(Model $model, User $user): void
    {
        $this->deviceRepository->save(
            (new Device())
                ->setMac($model->mac)
                ->setIpAddress($model->ip)
                ->setUser($user)
        );
    }

    public function getDevices(User $user): array
    {
        return $this->deviceRepository->findBy(['user' => $user->getId()]);
    }
}