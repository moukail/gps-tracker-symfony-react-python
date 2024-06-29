<?php

namespace App\Service;

use App\Entity\Device;
use App\Entity\Location;
use App\Model\LocationDto as Model;
use App\Repository\LocationRepository;

readonly class LocationService
{
    public function __construct(private LocationRepository $locationRepository)
    {}

    public function getLocations(Device $device): array
    {
        return $this->locationRepository->findBy(['device' => $device->getId()]);
    }

    public function create(Model $model, Device $device): void
    {
        $this->locationRepository->save(
            (new Location())
                ->setLatitude($model->latitude)
                ->setLongitude($model->longitude)
                ->setAltitude($model->altitude)
                ->setDevice($device)
        );
    }
}
